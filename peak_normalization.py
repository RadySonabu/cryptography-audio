audio_signal = [0, 0.23, -0.4]
print("Raw audio signal", audio_signal)
current_peak = max(audio_signal)
print("current peak:", current_peak)
target_db = 3
print("target db", target_db)
db = target_db - current_peak
print("db:", db)
g = pow(10, (db / 20))
print("G:", g)
output = [g * (1 / current_peak) * signal for signal in audio_signal]
print("Normalized audio signal", output)
