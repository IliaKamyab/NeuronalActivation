import pylsl
import time

def main():
    streams = pylsl.resolve_stream('name', 'PetalStream_eeg')
    inlet = pylsl.StreamInlet(streams[0])
    sample, timestamp_0 = inlet.pull_sample()

    while True:
        sample, timestamp = inlet.pull_sample()

        print(timestamp-timestamp_0)

if __name__ == '__main__':
    main()