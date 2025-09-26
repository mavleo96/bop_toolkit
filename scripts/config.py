from dataclasses import dataclass

@dataclass
class Config:
    eval_path = "/workspace/pose-estimation/results"
    results_path = "/workspace/pose-estimation/results"
    datasets_path = "/workspace/pose-estimation/datasets"
    num_workers = 4
    use_gpu = True