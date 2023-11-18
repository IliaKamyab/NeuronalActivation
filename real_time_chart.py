import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pylsl


# Create figure for plotting 5 different lines
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ys2 = []
ys3 = []
ys4 = []
ys5 = []

streams = pylsl.resolve_stream('name', 'PetalStream_eeg')
inlet = pylsl.StreamInlet(streams[0])
sample, timestamp_0 = inlet.pull_sample()
# This function is called periodically from FuncAnimation
def animate(i, xs, ys, ys2, ys3, ys4, ys5):
   
    
    sample, timestamp = inlet.pull_sample()
    xs.append(timestamp-timestamp_0)
    ys.append(sample[0])
    ys2.append(sample[1])
    ys3.append(sample[2])
    ys4.append(sample[3])
    ys5.append(sample[4])

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]
    ys2 = ys2[-20:]
    ys3 = ys3[-20:]
    ys4 = ys4[-20:]
    ys5 = ys5[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label='Channel 1')
    ax.plot(xs, ys2, label='Channel 2')
    ax.plot(xs, ys3, label='Channel 3')
    ax.plot(xs, ys4, label='Channel 4')
    ax.plot(xs, ys5, label='Channel 5')

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('EEG Data')
    plt.ylabel('Voltage (mV)')
    plt.xlabel('Time (s)')
    plt.legend(loc='upper left')
    plt.tight_layout()

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ys2, ys3, ys4, ys5), interval=5)
plt.show()



