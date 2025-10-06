"""
Compute perplexity using sliding window approach.
Taken from: https://huggingface.co/docs/transformers/en/perplexity
"""

import torch
from transformers import AutoModelForCausalLM, BatchEncoding, BarthezTokenizer
from tqdm.auto import tqdm
from utils.utils import open_md


def compute_ppl(
    model: AutoModelForCausalLM,
    encodings: BatchEncoding,
    max_length: int,
    seq_len: int,
    stride: int = 512,
    device: str = "cpu",
) -> tuple[float, float]:
    """
    Compute perplexity using sliding window approach.
    
    Returns:
        Tuple of (average_nll, perplexity)
    """
    nll_sum = 0.0
    n_tokens = 0
    prev_end_loc = 0
    for begin_loc in range(0, seq_len, stride):
        end_loc = min(begin_loc + max_length, seq_len)
        trg_len = end_loc - prev_end_loc  # may be different from stride on last loop
        input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
        target_ids = input_ids.clone()
        target_ids[:, :-trg_len] = -100

        with torch.no_grad():
            outputs = model(input_ids, labels=target_ids)

            # loss is calculated using CrossEntropyLoss which averages over valid labels
            # N.B. the model only calculates loss over trg_len - 1 labels, because it internally shifts the labels
            # to the left by 1.
            neg_log_likelihood = outputs.loss

        # Accumulate the total negative log-likelihood and the total number of tokens
        num_valid_tokens = (
            (target_ids != -100).sum().item()
        )  # number of valid tokens in target_ids
        batch_size = target_ids.size(0)
        num_loss_tokens = (
            num_valid_tokens - batch_size
        )  # subtract batch_size due to internal label shift
        nll_sum += neg_log_likelihood * num_loss_tokens
        n_tokens += num_loss_tokens

        prev_end_loc = end_loc
        if end_loc == seq_len:
            break

    avg_nll = nll_sum / n_tokens  # average negative log-likelihood per token
    ppl = torch.exp(avg_nll)

    return avg_nll.item(), ppl.item()


def compute_ppl_for_documents(
    max_length: int,
    stride: int,
    list_of_path: list[str],
    model: AutoModelForCausalLM,
    tokenizer: BarthezTokenizer,
    logger,
    device: str,
) -> list[tuple[str, float]]:
    """
    Compute perplexity for a list of text files.

    Returns:
        List of tuples (file_path, perplexity)
    """
    ppl_list = []
    for path in tqdm(list_of_path):
        try:
            text = open_md(path)
        except Exception as e:
            logger.error(f"Cannot open {path}: {e}")
            continue

        try:
            encodings = tokenizer(text, return_tensors="pt")
            seq_len = encodings.input_ids.size(1)

            _, ppl = compute_ppl(
                model,
                encodings,
                max_length,
                seq_len,
                stride,
                device,
            )

            ppl_list.append((path, ppl))

        except Exception as e:
            logger.error(f"Error computing perplexity for {path}: {e}")

    return ppl_list