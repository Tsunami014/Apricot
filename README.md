This is still in development, but look forward to v4.0.0!

## Quicklinks
| [Contents](#contents) | [Requirements](#system-requirements) | [Demos](#demos) | [Installation](#installation) | [Fun facts](#fun-facts) |
|:-:|:-:|:-:|:-:|:-:|

## Contents
The docs are located at [./docs](./docs/README.md)

Apricot is an engine of some kind for Python containing;

### A graphics module (with premade GUI elements!!)
- Which is faster than Pygame! (Compiled with cython) It's even faster than Pygame when displaying a blank screen, which is cool.
    - It uses vsync (but can be turned off) which prevents it from taking up 100% cpu drawing frames that the monitor isn't even fast enough to display
- Is very "Pythonic", including type hints, docstrings and magic methods!
- Uses an "operation stack", so instead of Pygame's approach of running each transformation on surfaces one by one, generating intermediate surfaces along the way, it applies all operations onto one output buffer at once! (Combining some operations too like transformations)
- Comes with many GUI elements for ease of use!

### A collision engine
- Can collide various shapes (e.g. points, lines, circles, rectangles, etc.) efficiently (compiled with cython)
- Has built-in functions for handling how shapes collide with other shapes when moving, so you don't have to worry!
- Uses complex maths to calculate where objects hit each other when moving and calculates rebound position and velocity, so *clipping through shapes is impossible*

### Various utils
Including:

#### An image wrapper
- There is a base shape creator, which takes a bunch of points and wraps it into a closed polygon.
- And then you can use this with images to wrap images into shapes!
- This is made with just numpy and is compiled with cython for speed

### Many old things I need to improve/remove/add to
Yes, this project is extremely still in development. But v4.0.0 should be fully working! Look forward to it!

## System requirements
- Python 3.11+
- Linux or Windows
    - Although, I don't test on Windows - but feel free to make a PR if there's a problem

## Demos
To run the demos;

1. Clone the repo (with `--depth 5` so you're not pulling all of history)
2. Install requirements
3. Run `python3 demos`

```bash
git clone --depth 5 https://github.com/Tsunami014/Apricot.git
cd apricot
pip install .
python3 demos
```

## Installation
`pip install apri`

### Installing from sauce 🍅
- Git clone and pip install (`--depth 5` clones only the most recent 5 commits, because the history of this project is huge)
```bash
git clone --depth 5 https://github.com/Tsunami014/Apricot.git
cd apricot
pip install .
```

- OR use the one liner
```bash
pip install "git+https://github.com/Tsunami014/Apricot.git"
```


## Fun facts
- This project was made entirely by one person! (So far)
- This project was started before AI existed (back in ye olde 2023/2024, origins are debatable), and many features, including the whole physics engine and image wrapping, were created entirely by me without help from AI in any way (because it wasn't good enough to help at all).
- I turned/will turn (not bothered to change this lol) 18 in 2027. So that means I also made the physics engine etc. before I was/am an adult. Which is my greatest flex hehe
- Because this project is so old (in terms of my life), I changed coding styles a LOT during development, and because it's so big there's a chance you can find some places where my old code still is unfortunately
- I tried to use as little external libraries as possible, mostly because I didn't want this to end up like some projects where it has to install a million different things. Also fits with the theme of 'making stuff all myself from scratch'.
- This project used to be called Blaze Sudio (mistake intentional) before v4.0.0
