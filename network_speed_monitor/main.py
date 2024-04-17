import speedtest
import time


def network_monitor_speed(interval_seconds=60):
    st = speedtest.Speedtest()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    print(f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")
    # while True:
    #     download_speed = st.download() / 1_000_000
    #     upload_speed = st.upload() / 1_000_000

    #     print(
    #         f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")

    #     time.sleep(interval_seconds)


def main():
    network_monitor_speed()



if __name__ == "__main__":
    # You can customize the interval_seconds parameter as needed (default is 60 seconds)
    main()
