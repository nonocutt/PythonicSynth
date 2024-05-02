"""
This Python script creates a synthesizer setup using the Pyo library, specifically designed to handle MIDI inputs and generate complex soundscapes with various waveforms and effects. The program initializes a MIDI-controlled synthesizer with ADSR envelope shaping and provides real-time GUI controls for waveform selection and effect parameters adjustment. It includes multiple oscillators with different waveforms, a low-pass filter, reverb, and chorus effects for each oscillator channel.

To run this program:
1. Ensure Pyo and a MIDI input device are properly configured on your system.
2. Execute this script. The Pyo server will start, and a GUI will appear for real-time control.
3. Play MIDI notes through the input device, and use the GUI to manipulate the synthesizer's sound dynamically.
"""

from pyo import *

# Initialize the server, boot it, and start it
s = Server().boot().start()
s.setMidiInputDevice(99)     # Set MIDI input device to global

# Setup MIDI input
notes = Notein(scale=1)      # Convert MIDI to Hz
notes.keyboard()             # Display a MIDI keyboard on GUI

# Setup ADSR envelope for dynamics control
env = MidiAdsr(notes["velocity"], attack=0.005, decay=0.1, sustain=0.7, release=0.01, mul=1)
env.ctrl(title="Envelope Shape")  # Control interface for the envelope

# Frequency signals for oscillators
freq1 = Sig(1)
freq2 = Sig(2)
freq3 = Sig(3)
freq4 = Sig(4)
freq5 = Sig(5)
freq6 = Sig(6)

# Initialize control signals for effects
cutoff_freq = Sig(500)       # Low-pass filter cutoff frequency
cutoff_res = Sig(0.5)        # Low-pass filter resonance
reverb_room_size = Sig(0.5)  # Reverb room size
reverb_damping = Sig(0.5)    # Reverb damping factor
chorus_depth = Sig(1.0)      # Chorus effect depth
chorus_feedback = Sig(0.25)  # Chorus feedback amount
reverb_drywet = Sig(1.0)     # Reverb dry/wet mix
chorus_drywet = Sig(1.0)     # Chorus dry/wet mix

# Different waveforms
def create_oscillators(freq):
    return [
        SineLoop(freq=notes["pitch"] * freq / 261.6, mul=env),
        SuperSaw(freq=notes["pitch"] * freq / 261.6, mul=env),
        Blit(freq=notes["pitch"] * freq / 261.6, mul=env),
        RCOsc(freq=notes["pitch"] * freq / 261.6, mul=env),
    ]

# Generate oscillators for each frequency
oscillators1 = create_oscillators(freq1 * 261.6)
oscillators2 = create_oscillators(freq2 * 261.6)
oscillators3 = create_oscillators(freq3 * 261.6)
oscillators4 = create_oscillators(freq4 * 261.6)
oscillators5 = create_oscillators(freq5 * 261.6)
oscillators6 = create_oscillators(freq6 * 261.6)

# Selector for choosing waveforms
sel1 = Selector(oscillators1)
sel2 = Selector(oscillators2)
sel3 = Selector(oscillators3)
sel4 = Selector(oscillators4)
sel5 = Selector(oscillators5)
sel6 = Selector(oscillators6)

# Low-pass filter
lpf1 = MoogLP(sel1, freq=cutoff_freq, res=cutoff_res)
lpf2 = MoogLP(sel2, freq=cutoff_freq, res=cutoff_res)
lpf3 = MoogLP(sel3, freq=cutoff_freq, res=cutoff_res)
lpf4 = MoogLP(sel4, freq=cutoff_freq, res=cutoff_res)
lpf5 = MoogLP(sel5, freq=cutoff_freq, res=cutoff_res)
lpf6 = MoogLP(sel6, freq=cutoff_freq, res=cutoff_res)

# Reverb
reverb1 = Freeverb(lpf1, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)
reverb2 = Freeverb(lpf2, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)
reverb3 = Freeverb(lpf3, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)
reverb4 = Freeverb(lpf4, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)
reverb5 = Freeverb(lpf5, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)
reverb6 = Freeverb(lpf6, size=reverb_room_size, damp=reverb_damping, mul=0.5, bal=reverb_drywet)

# Chorus
chorus1 = Chorus(reverb1, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)
chorus2 = Chorus(reverb2, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)
chorus3 = Chorus(reverb3, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)
chorus4 = Chorus(reverb4, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)
chorus5 = Chorus(reverb5, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)
chorus6 = Chorus(reverb6, depth=chorus_depth, feedback=chorus_feedback, mul=0.5, bal=chorus_drywet)

# 2-channel stereo output
pan1 = Pan(chorus1, outs=2, pan=0.5).out()
pan2 = Pan(chorus2, outs=2, pan=0.5).out()
pan3 = Pan(chorus3, outs=2, pan=0.5).out()
pan4 = Pan(chorus4, outs=2, pan=0.5).out()
pan5 = Pan(chorus5, outs=2, pan=0.5).out()
pan6 = Pan(chorus6, outs=2, pan=0.5).out()

# GUI controls for selector and effects
sel1.ctrl(title="OSC 1 Selector")
sel2.ctrl(title="OSC 2 Selector")
sel3.ctrl(title="OSC 3 Selector")
sel4.ctrl(title="OSC 4 Selector")
sel5.ctrl(title="OSC 5 Selector")
sel6.ctrl(title="OSC 6 Selector")

freq1.ctrl([SLMap(0.5, 32, "log", "value", 1)], title="OSC 1 Frequency")
freq2.ctrl([SLMap(0.5, 32, "log", "value", 2)], title="OSC 2 Frequency")
freq3.ctrl([SLMap(0.5, 32, "log", "value", 4)], title="OSC 3 Frequency")
freq4.ctrl([SLMap(0.5, 32, "log", "value", 6)], title="OSC 4 Frequency")
freq5.ctrl([SLMap(0.5, 32, "log", "value", 8)], title="OSC 5 Frequency")
freq6.ctrl([SLMap(0.5, 32, "log", "value", 10)], title="OSC 6 Frequency")

cutoff_freq.ctrl([SLMap(200, 5000, "log", "value", 1000)], title="LPF Cutoff Frequency")
cutoff_res.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.0)], title="LPF Resonance")
reverb_room_size.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.5)], title="Reverb Room Size")
reverb_damping.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.5)], title="Reverb Damping")
reverb_drywet.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.25)], title="Reverb Dry/Wet")
chorus_depth.ctrl([SLMap(0.0, 0.25, "lin", "value", 0.1)], title="Chorus Depth")
chorus_feedback.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.5)], title="Chorus Feedback")
chorus_drywet.ctrl([SLMap(0.0, 1.0, "lin", "value", 0.0)], title="Chorus Dry/Wet")

# Launch the GUI for real-time control
s.gui(locals())
