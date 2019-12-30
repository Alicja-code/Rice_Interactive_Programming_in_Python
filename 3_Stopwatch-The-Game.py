# "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
x = 0  # successful stops
y = 0  # total stops
running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t % 10
    t //= 10
    bc = t % 60
    t //= 60
    a = t
    return '%d:%02d.%d' % (a, bc, d)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True


def stop():
    global running, x, y
    if running:
        timer.stop()
        running = False
        y += 1
        if counter % 10 == 0:
            x += 1


def reset():
    global counter, x, y, running
    counter, x, y, running = 0, 0, 0, False
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1


# define draw handler
def draw(canvas):
    global counter, x, y
    counter_formatted = format(counter)
    canvas.draw_text(counter_formatted, [90, 120], 48, "Aqua")
    canvas.draw_text('%d/%d' % (x, y), [230, 50], 30, "Lime")


# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
