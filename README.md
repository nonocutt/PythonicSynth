# PythonicSynth

Welcome to the **PythonicSynth** User Manual. **PythonicSynth** is an additive synthesizer with six oscillators that allow for wave selection. This manual will guide you through the features of **PythonicSynth** and how to use them.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
  - [MIDI Input](#midi-input)
  - [Envelope Shape](#envelope-shape)
  - [OSC Selectors](#osc-selectors)
  - [OSC Frequency](#osc-frequency)
  - [Effectors](#effectors)
- [Example](#example)
- [FAQ](#faq)
- [Contact](#contact)

## Getting Started

- To use **PythonicSynth**, you need to install [pyo](https://pypi.org/project/pyo/) first.

    ```unix
    pip install pyo
    ```

  - For Python 3, run:

  ```unix
  pip3 install pyo
  ```

- **PythonicSynth** requires additional libraries to run:
  - [FLAC](https://xiph.org/flac/)
  - [Vorbis](https://xiph.org/vorbis/)
  - [Opus](https://www.opus-codec.org/)
  - [mpg123](https://www.mpg123.de/)
  - [LAME](https://lame.sourceforge.io/)
  - [wxPython](https://www.wxpython.org/)
- If you are using [homebrew](https://brew.sh/), you can run the following code in the terminal to proceed:

  ```unix
  brew install flac
  brew install libvorbis
  brew install opus
  brew install mpg123
  brew install lame
  brew install wxpython
  ```

- Here is the interface of the program:

![screenshot](PythonicSynth.jpg)

## Features

### MIDI Input

- **PythonicSynth** can receive MIDI note and velocity signal from all channels and convert them to corresponding frequency and volume.

  - You can also use Z row and Q row on the QWERTY keyboard as an alternative input method.

- 10 notes can be pressed at a single time.

### Envelope Shape

- An *envelope generator* shapes how the sound's amplitude (loudness) evolves over time from when a note is played until it ends.
  - **Attack** is the time it takes for the sound to reach its maximum level after a note is triggered.
  - **Decay** is how long it takes for the sound to reduce to the sustain level.
  - **Sustain** is the level at which the sound remains until the key is released.
  - **Release**  determines how long the sound takes to fade out from the sustain level to silence.
  - **Exp** stands for *exponential*, alters the shape of the envelope curve.

### OSC Selectors

- **PythonicSynth** provides 4 types of waveform: sine, saw, pulse, and square. They can be adjusted by changing the *voice* value to 0, 1, 2, and 3. Changing the value to a decimal will result a combination of 2 waveforms.

- You can adjust the volume of each oscillator by changing the *mul* value on the OSC selectors.

### OSC Frequency

- The OSC frequency value is a multiplier, based on the key you pressed on the MIDI input.

  - For examble, 2.000 means 2x frequency of the input note, which results an octave higher.

### Effectors

- **PythonicSynth** has 3 types of effectors, which are low-pass filter, reverb, and chorus.

  - *LPF* is a simulation of the **Moog VCF**, giving a decay of 24dB/oct. You can control the cutoff frequency and resonance in the module.
  - *Reverb* is based on based on Jezar's **Freeverb**. You can adjust the reverb size and damping in the module.
  - *Chorus* has 8 modulated delay lines. You can control the depth and feedback in the module.

## Example

### Simple Square Wave

  ```python
  OSC 1 voice = 0, mul = 1, freq = 1
  OSC 2 voice = 0, mul = 0.333, freq = 3
  OSC 3 voice = 0, mul = 0.2, freq = 5
  OSC 4 voice = 0, mul = 0.143, freq = 7
  OSC 5 voice = 0, mul = 0.111, freq = 9
  OSC 6 voice = 0, mul = 0.091, freq = 11
  ```

### Hammond Organ

  ```python
  OSC 1 voice = 0, mul = 1, freq = 0.5
  OSC 2 voice = 0, mul = 0.75, freq = 1.5
  OSC 3 voice = 0, mul = 0.625, freq = 1
  OSC 4 voice = 0, mul = 0.5, freq = 5
  OSC 5 voice = 0, mul = 0.75, freq = 6
  OSC 6 voice = 0, mul = 0.875, freq = 8
  ```

## FAQ

### Will there be additional features/updates in the future?

This is a prototype for my class project. The project is no longer being maintained and there are no plans for any further updates at this moment.

### I found a bug. How can I report it?

Since this is no longer being maintained, I am not accepting reports at this time.
This is an academic project, not a fully polished product, so please use at your own risk.

## Contact

© nonocut 2024, 2025

[Drop a line](https://nonocut.com/contact/)
