"use strict";

$(function () {
  $("#reservation_date").val(new Date().toISOString().slice(0, 10));
});

// Delete reservation
function deleteItem(id) {
  let url = `/reservations/delete/${id}`;

  fetch(url, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((result) => {
      console.log("result: ", result);
      if (result["success"] === true) {
        document.querySelector(`#reservation-row-${id}`).remove();
      }
    });
}

function availableTimeSlots(e) {
  let reservation_date = e.target.value;

  document.querySelectorAll(".btn-sm").forEach((button) => {
    button.setAttribute("disabled", "");
  });

  let url = `/time_slots/${reservation_date}`;

  fetch(url, {
    method: "POST",
  })
    .then((responce) => responce.json())
    .then((result) => {
      if (result["success"] === true) {
        result["timeslots"].forEach((timeslot) => {
          // console.log(
          //   "timeslot: ",
          //   timeslot,
          //   " selector: ",
          //   `.btn-sm[value='${timeslot}']`
          // );
          document
            .querySelector(`.btn-sm[value='${timeslot}']`)
            .removeAttribute("disabled");
        });
      }
    });
}

// Hidden input (#timeslot) since buttons can't pass the values
function timeslotSelected(e) {
  document.querySelector("#timeslot").value = e.value;
}
