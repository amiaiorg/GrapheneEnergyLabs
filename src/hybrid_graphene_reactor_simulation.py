
import numpy as np
from quantum_reactor_simulation import QuantumReactor

class HybridGrapheneReactor(QuantumReactor):
    def __init__(self, num_particles=1000, subspace_dimensions=11, interaction_strength=0.1, base_frequency=1e15):
        super().__init__(num_particles, subspace_dimensions, interaction_strength, base_frequency)
        self.alpha_capture_efficiency = 0.93
        self.proton_capture_efficiency = 0.85

    def capture_alpha_particles(self, fusion_events):
        captured_alpha = fusion_events * self.alpha_capture_efficiency
        return captured_alpha

    def capture_protons(self, fusion_events):
        captured_protons = fusion_events * self.proton_capture_efficiency
        return captured_protons

    def convert_energy(self, captured_alpha, captured_protons):
        total_captured = captured_alpha + captured_protons
        converted_energy = total_captured * self.fusion_energy
        return converted_energy

    def run_hybrid_simulation(self, duration, time_steps):
        t, states, energy_outputs = self.run_simulation(duration, time_steps)

        total_captured_alpha = 0
        total_captured_protons = 0
        total_converted_energy = 0

        for i in range(len(t)):
            fusion_events = self.fusion_reaction(states[i].reshape((self.num_particles, self.subspace_dimensions)))
            captured_alpha = self.capture_alpha_particles(fusion_events)
            captured_protons = self.capture_protons(fusion_events)
            converted_energy = self.convert_energy(captured_alpha, captured_protons)

            total_captured_alpha += np.sum(captured_alpha)
            total_captured_protons += np.sum(captured_protons)
            total_converted_energy += converted_energy

        average_power = total_converted_energy / duration

        print(f"Hybrid Graphene Reactor Simulation Results:")
        print(f"Total Converted Energy: {total_converted_energy:.2f} MeV")
        print(f"Average Power Output: {average_power:.2f} MeV/s")
        print(f"Total Captured Alpha Particles: {total_captured_alpha:.2f}")
        print(f"Total Captured Protons: {total_captured_protons:.2f}")

        return t, states, total_converted_energy, total_captured_alpha, total_captured_protons

if __name__ == "__main__":
    reactor = HybridGrapheneReactor()
    duration = 1e-12  # 1 picosecond
    time_steps = 1000
    reactor.run_hybrid_simulation(duration, time_steps)
