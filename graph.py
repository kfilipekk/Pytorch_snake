import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import threading
import queue
import time

##Thread-safe plotting
plot_queue = queue.Queue()
plot_thread = None
fig = None

def _plot_worker():
    """Worker function that runs in a separate thread"""
    global fig
    matplotlib.use('TkAgg')
    
    fig = plt.figure(figsize=(10, 6))
    plt.ion()
    plt.show(block=False)
    
    while True:
        try:
            data = plot_queue.get(timeout=1)
            if data is None:
                break
                
            scores, mean_scores = data
            
            plt.figure(fig.number)
            plt.clf()
            
            plt.title('Training Progress')
            plt.xlabel('Loops')
            plt.ylabel('Score')
            
            if scores:
                plt.plot(scores, label='Score', linestyle='-', color='blue', linewidth=1)
            if mean_scores:
                plt.plot(mean_scores, label='Mean Score', linestyle='--', color='orange', linewidth=2)
            
            plt.ylim(ymin=0)
            plt.grid(True, linestyle='--', alpha=0.3)
            plt.legend()
            
            if scores and len(scores) > 0:
                plt.text(len(scores) - 1, scores[-1], f"{scores[-1]}", ha='center', va='bottom', fontsize=8, color='blue')
            if mean_scores and len(mean_scores) > 0:
                plt.text(len(mean_scores) - 1, mean_scores[-1], f"{mean_scores[-1]:.1f}", ha='center', va='bottom', fontsize=8, color='orange')
            
            fig.canvas.draw()
            fig.canvas.flush_events()
            
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Plot error: {e}")
            continue

def plot(scores, mean_scores):
    global plot_thread
    
    if plot_thread is None or not plot_thread.is_alive():
        plot_thread = threading.Thread(target=_plot_worker, daemon=True)
        plot_thread.start()
        time.sleep(0.1)
    
    try:
        plot_queue.put((scores[:], mean_scores[:]), block=False)
    except queue.Full:
        pass
