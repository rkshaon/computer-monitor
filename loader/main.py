from tqdm import tqdm
import time



def custom_loader():
    # generating custom loader
    for i in tqdm(range(100)):
        # Your long-running process here
        time.sleep(0.1)  # Simulate some work


def main():
    custom_loader()



if __name__ == "__main__":
    main()