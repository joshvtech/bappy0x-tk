$(document).ready(function() {
    $("[data-toggle=\"tooltip\"]").tooltip();

    $.ajax("https://api.bappy0x.tk/notifications")
    .done(function(data) {
        if ("valid" in data) {
            data.valid.forEach(notif => {
                $("#notifications").append(
                    `<div class="toast" id="${notif.id}" role="alert" data-autohide="false">
                        <div class="toast-header">
                            <strong class="mr-auto">${notif.head}</strong>
                            ${notif.timestamp ? `<small class=\"text-muted\">${moment(notif.timestamp).fromNow()}</small>` : ""}
                            ${notif.important ? "<span class=\"badge badge-danger ml-1\">Important</span>" : ""}
                            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast">
                                <i class="fas fa-times"></i>
                            </button>
                        </div>
                        <div class="toast-body">${notif.body}</div>
                    </div>`
                );
                $(`.toast#${notif.id}`).toast("show");
            });
        } else {
            console.error("Couldn't find valid notifications!")
        };
    })
    .fail(function(_, textStatus) {
        console.error(`Notifications GET failed: "${textStatus}".`);
    });
});