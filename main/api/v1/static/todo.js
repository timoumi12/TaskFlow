const form = document.getElementById("todo-form");
const input = document.getElementById("todo-input");
const todoLane = document.getElementById("todo-lane");
const modal = document.getElementById("myModal");
const save = document.getElementById("save_btn");


form.addEventListener("submit", (e) => {
    e.preventDefault();
    const value = input.value;

    // Set the value of the hidden input in the second form
    document.getElementById('todo-title').value = value;
    
    console.count(value);

    if (!value) return;
    openModal(value);

    const newTask = document.createElement("button");
    newTask.classList.add("task");
    newTask.setAttribute("draggable", "true");
    newTask.innerText = value;

    newTask.addEventListener("click", () => {
        openModal(value);
    });

    newTask.addEventListener("dragstart", () => {
        newTask.classList.add("is-dragging");
    });

    newTask.addEventListener("dragend", () => {
        newTask.classList.remove("is-dragging");
    });

    todoLane.appendChild(newTask);
    input.value = "";
});

function openModal(taskDetails) {
    
    modal.style.display = "block";
}

function closeModal() {
    modal.style.display = "none";
}

// Close the modal if the user clicks outside the modal content
window.onclick = function(event) {
    if (event.target === modal) {
        closeModal();
    }
}




