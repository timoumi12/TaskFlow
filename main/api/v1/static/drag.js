const draggables = document.querySelectorAll(".task");
const droppables = document.querySelectorAll(".swim-lane");

draggables.forEach((task) => {
  task.addEventListener("dragstart", () => {
    task.classList.add("is-dragging");
  });
  task.addEventListener("dragend", () => {
    task.classList.remove("is-dragging");
  });
});

droppables.forEach((zone) => {
  zone.addEventListener("dragover", (e) => {
    e.preventDefault();

    const bottomTask = insertAboveTask(zone, e.clientY);
    
    const curTask = document.querySelector(".is-dragging");


    // Update the state attribute based on the swim lane (column) being dragged over
    switch (zone.id) {
      case "todo-lane":
        updateTaskState(curTask, "todo");
        break;
      case "doing-lane":
        updateTaskState(curTask, "doing");
        break;
      case "done-lane":
        updateTaskState(curTask, "done");
        break;
    }

    if (!bottomTask) {
      zone.appendChild(curTask);
    } else {
      zone.insertBefore(curTask, bottomTask);
    }
  });
});

const insertAboveTask = (zone, mouseY) => {
  const els = zone.querySelectorAll(".task:not(.is-dragging)");

  let closestTask = null;
  let closestOffset = Number.NEGATIVE_INFINITY;

  els.forEach((task) => {
    const { top } = task.getBoundingClientRect();

    const offset = mouseY - top;

    if (offset < 0 && offset > closestOffset) {
      closestOffset = offset;
      closestTask = task;
    }
  });

  return closestTask;
};

const updateTaskState = async (taskElement, newState) => {
  const taskId = taskElement.getAttribute("data-task-id");

  try {
    const response = await fetch(`/update_task_state/${taskId}/${newState}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      console.log("Task state updated successfully");
    } else {
      console.error("Failed to update task state");
    }
  } catch (error) {
    console.error("Error updating task state:", error);
  }
};
