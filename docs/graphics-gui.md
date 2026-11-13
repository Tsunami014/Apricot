> [!NOTE]
> This was designed to be functionally similar to [the core graphics module](./graphics-core.md), but *do not mix them*.

# Basic structure
1. Setup (e.g. run `UI.fullscreen()`)
2. Set layout `UI(...)`
3. Run mainloop `UI.Run()` (can combine with previous step; `UI(...).Run()`)

# `apricot.GUI` contents
## `UI`
> The main screen object, functionally identical to `apricot.graphics.Core` except it uses GUI elements instead of graphics operations, and handles the mainloop in a convenient `Run` function.

This is a singleton object created when `apricot.GUI` is imported, you do not need to run any setup code.

<!-- GUI.UI -->
- `__new__`
- `__init__`
- `_init`
- `_arr`
- `_sze`
- `op`
- `smooth`
- `_vsync`
- `_mainWin`
- `Quit`: Quits the application, handling all quit code accordingly.

This is useful to include at the end of your program as it closes the window much faster than if you don't include it.
- `resize`
- `fullscreen`: Resize the window to fullscreen.

A wrapper for `Core.resize()`
- `_find_size`
- `__del__`
- `size`
- `width`
- `height`
- `resizable`
- `vsync`: If True, the frame rate will be capped at whatever the refresh rate of the monitor is
If False, the program will run as fast as possible and chew up CPU displaying frames that won't even be rendered because the monitor can't display that fast

Defaults to True
- `rebuild`
- `_resize_event`
- `rend`: Render the entire screen by writing directly to SDL memory.
- `clear`
- `redraw`
- `title`
- `set_icon`
- `bgcol`
- `clock`
- `cursor`
- `__call__`
- `Run`: Handles the basic interaction loop, including clock ticking and rendering

Basically just a wrapper for a lot of common stuff.

Keyword args:
    quit_after: If True, after exiting will quit (speeds up window closing)
    fps_title: If True, every frame it will set the window title to the current average FPS. For debugging
- `clearFocus`: Clears the focus from all elements
<!--! GUI.UI -->