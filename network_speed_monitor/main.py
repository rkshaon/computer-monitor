import speedtest
import time

from loader import main as loader_main


def get_network_speed_data(interval_seconds=60):
    st = speedtest.Speedtest()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    # print(f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")
    return f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps"


def main():
    network_speed_data = None
    network_speed_data = get_network_speed_data()
    loader_main.main()
    print(network_speed_data)



if __name__ == "__main__":
    main()
