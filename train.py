import torch

def main():
    print("PyTorch version:", torch.__version__)
    print("Device:", "cuda" if torch.cuda.is_available() else "cpu")

    x = torch.tensor([1, 2, 3, 4, 5])

    print('tensor', x)
    print("shape", x.shape)


if  __name__ == "__main__":
    main()
