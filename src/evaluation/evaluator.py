from metrics.accuracy import calculate_accuracy

def run_evaluation(correct, total):
    accuracy = calculate_accuracy(correct, total)

    return {
        "accuracy": accuracy
    }
