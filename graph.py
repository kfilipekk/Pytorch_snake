import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    
    plt.figure(figsize=(8, 5))
    plt.title('Training Progress')
    plt.xlabel('Episodes')
    plt.ylabel('Q-Value')
    
    plt.plot(scores, label='Score', linestyle='-', marker='o', markersize=4)
    plt.plot(mean_scores, label='Mean Score', linestyle='--', color='orange')
    
    plt.ylim(ymin=0)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    if scores:
        plt.text(len(scores) - 1, scores[-1], f"{scores[-1]:.2f}", ha='right', fontsize=10, color='blue')
    if mean_scores:
        plt.text(len(mean_scores) - 1, mean_scores[-1], f"{mean_scores[-1]:.2f}", ha='right', fontsize=10, color='orange')
    
    plt.show(block=False)
    plt.pause(0.1)
