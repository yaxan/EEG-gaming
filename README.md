# EEG gaming
Work in progress: DIY Brain-Computer Interface (BCI) to play games using alpha/beta waves with custom-made EEG circuit.

More details on how it works and how to replicate coming soon.

## Live Flappy-Bird Demo
https://user-images.githubusercontent.com/41130598/219846836-aeb79bd7-619f-477f-9fea-56bf63279e5b.mp4

## Circuit

### Overview
  This circuit is designed to take the differntial input of the FP2 and O2 regions on the brain, amplify signals from ~8-32Hz, and send to the Raspberry Pi for processing. It uses a combination of instrument amplifiers, high pass, low pass, and notch filters to filter and amplify the signals before they are sent to the ADC to conver the signal from analog to digital which the Raspberry Pi can then process.

### Parts List
 * 2x AD623AN Instrument Amplifier
 * 4x LM471CN Operational Amplifier
 * 2x 150kΩ Resistor
 * 1x 1.1kΩ Resistor
 * 8x 220nF Capacitor
 * 4x 12kΩ Resistor
 * 4x 5.6kΩ Resistor
 * 2x 22kΩ Resistor
 * 2x 402Ω Resistor (Use 1x 200Ω Instead)
 * 1x 0-2kΩ Potentiometer
 * [3x OpenBCI Gold Cup Electrodes](https://shop.openbci.com/products/openbci-gold-cup-electrodes?_pos=1&_sid=645e136ca&_ss=r)
 * [Ten20 Conductive Neurodiagnostic Electrode Paste](https://shop.openbci.com/products/ten20-conductive-paste-8oz-jar)
 * Adafruit ADS1115 16-Bit ADC
 * Raspberry Pi 4 Model B 4GB RAM
 * Medical Tape (To stick on electrodes)
 * Keithley 2231A-30-3 Triple Channel DC Power Supply (Batteries work too)

### Schematic
![EEGSchematic](https://user-images.githubusercontent.com/41130598/221042409-423589c1-2b3c-4a02-94aa-657f63461b93.png)
Warning: Connecting electrodes to any part of your body can result in shock if anything goes wrong with the circuit, there are no safety features implemented to use at your own discretion.

  Three electrodes are used, one at the FP2 region (one inch up from the naison and one inch right), one at the O2 region (one inch up from the inion and one inch right), and one on the earlobe or mastoid which connects to 3.3V ground. It's important to note the voltage values for the IAs and Op-Amps are with respect to the RPI's 3.3V ground, while the ADC uses the RPI's 0V ground. This is to up-shift the signal from the brain because the ADC does not handle negative values well, it's then shifted back down in the code. If you are attempting to reconstruct this circuit, it's important to have access to an oscilloscope and wave-function generator to debug and test it works fine before connecting to electrodes/ADC/RPI.

Stage 1: Instrument Amplifier (Gain: ~92)

Stage 2: Notch Filter (Gain: 1, Cutoff frequency: ~60Hz)

Stage 3: High-Pass Filter (Gain: 1, Cutoff frequency: ~5Hz)

Stage 4: Low-Pass Filter (Gain: 1, Cutoff frequency: ~33Hz)

Stage 5: Instrument Amplifier (Gain: ~46-500)

Stage 6: Notch Filter (Gain: 1, Cutoff frequency: ~60Hz)


### Physical Circuit
![EEG-circuit](https://user-images.githubusercontent.com/41130598/219847191-df59c969-152d-49f6-9052-b21f6ea1c098.png)

## Credits

This project was based on the guidance from https://github.com/ryanlopezzzz/EEG with a modified circuit and new code for data-gathering, analysis, and gameplay. The repository had amazing explanations for everything and Ryan was great help when we reached out to him with questions. Much of their code no longer works as of January 2023 so we hope our project can help others replicate something similar for getting started with BCIs and EEG.
