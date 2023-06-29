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
            num_frames = int(request.POST["frames"])
            numbers = [int(num) for num in numbers_input]

            result1, total_faults1 = fifo(numbers, num_frames)
            result2, total_faults2 = lru(numbers, num_frames)
            result3, total_faults3 = lfu(numbers, num_frames)
            result4, total_faults4 = mfu(numbers, num_frames)

            for i, step in enumerate(result1, start=1):
                step["step"] = i

            for i, step in enumerate(result2, start=1):
                step["step"] = i

            for i, step in enumerate(result3, start=1):
                step["step"] = i

            for i, step in enumerate(result4, start=1):
                step["step"] = i

            min_faults = min(total_faults1, total_faults2, total_faults3, total_faults4)
            best_algorithms = []
            if total_faults1 == min_faults:
                best_algorithms.append("FIRST IN FIRST OUT ALGORITHM")
            if total_faults2 == min_faults:
                best_algorithms.append("LEAST RECENTLY USED ALGORITHM")
            if total_faults3 == min_faults:
                best_algorithms.append("LEAST FREQUENTLY USED ALGORITHM")
            if total_faults4 == min_faults:
                best_algorithms.append("MOST FREQUENTLY USED ALGORITHM")

            return render(
                request,
                "processing.html",
                {
                    "result1": result1,
                    "total_faults1": total_faults1,
                    "result2": result2,
                    "total_faults2": total_faults2,
                    "result3": result3,
                    "total_faults3": total_faults3,
                    "result4": result4,
                    "total_faults4": total_faults4,
                    "best_algorithms": best_algorithms,
                },
            )

    return render(request, "home.html")
