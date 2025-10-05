import torch
# from tqdm.auto import tqdm
from transformers import (
    AutoModelForCausalLM, 
)

def compute_ppl(
    model:AutoModelForCausalLM,
    tokenizer,
    encodings: dict[str, torch.Tensor],
    max_length: int,
    seq_len: int,
    stride:int=512,
    device="cpu",
) -> tuple[float, float]:
    """
    Compuet ppl for 1 document
    """

    # print(f"num gpu use: {torch.cuda.device_count()}")
    
    nll_sum = 0.0
    n_tokens = 0
    prev_end_loc = 0
    # print("begine looping")
    # for begin_loc in tqdm(range(0, seq_len, stride)):
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
        num_valid_tokens = (target_ids != -100).sum().item()  # number of valid tokens in target_ids
        batch_size = target_ids.size(0)
        num_loss_tokens = num_valid_tokens - batch_size  # subtract batch_size due to internal label shift
        nll_sum += neg_log_likelihood * num_loss_tokens
        n_tokens += num_loss_tokens
    
        prev_end_loc = end_loc
        if end_loc == seq_len:
            # print("exit")
            break

    # print("compute avg nll and ppl")
    avg_nll = nll_sum / n_tokens  # average negative log-likelihood per token
    ppl = torch.exp(avg_nll)

    return avg_nll.item() , ppl.item()