from django.shortcuts import render
from .forms import AlgorithmForm
from .algorithms import fifo, lru, lfu, mfu


def home(request):
    form = AlgorithmForm()
    return render(request, "home.html", {"form": form})


def processing(request):
    if request.method == "POST":
        form = AlgorithmForm(request.POST)

        if form.is_valid():
            numbers_input = request.POST["numbers"]
            algorithm = request.POST["algorithm"]
            num_frames = int(request.POST["frames"])
            numbers = [int(num) for num in numbers_input]

            result = []
            total_faults = 0

            if algorithm == "FIFO":
                result, total_faults = fifo(numbers, num_frames)
            elif algorithm == "LRU":
                result, total_faults = lru(numbers, num_frames)
            elif algorithm == "LFU":
                result, total_faults = lfu(numbers, num_frames)
            else:
                result, total_faults = mfu(numbers, num_frames)

            # Add step numbers to result
            for i, step in enumerate(result, start=1):
                step["step"] = i

            return render(
                request,
                "processing.html",
                {
                    "algorithm": algorithm,
                    "result": result,
                    "total_faults": total_faults,
                },
            )

    return render(request, "processing.html")
