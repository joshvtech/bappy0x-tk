$(document).ready(function() {
    $("[data-toggle=\"tooltip\"]").tooltip();

    $("#scrollToTopLink").click(function () {
        $("#top")[0].scrollIntoView({behavior: "smooth"});
        return false;
    });

    function getShownNotifications() {
        var raw = localStorage.getItem("shownNotifications");
        if (raw == null) {
            localStorage.setItem("shownNotifications", "[]");
            return [];
        } else {
            return JSON.parse(raw);
        };
    };

    $.ajax("https://api.bappy0x.tk/notifications/list")
    .done(data => {
        if ("notifs" in data) {
            if (typeof(Storage) !== "undefined") {
                var shown = getShownNotifications();
                data.notifs.forEach(notif => {
                    if (shown.includes(notif.id)) return;
                    $("#notifications").append(
                        `<div class="toast" id="${notif.id}" role="alert" data-autohide="false">
                            <div class="toast-header">
                                <strong class="mr-auto">${notif.head}</strong>
                                ${notif.timestamp ? `<small class=\"text-muted\">${moment(notif.timestamp).fromNow()}</small>` : ""}
                                ${notif.important ? "<span class=\"badge badge-danger ml-1\">Important</span>" : ""}
                                <button type="button" class="ml-2 mb-1 close" style="font-size: 0.8rem;" data-dismiss="toast">
                                    <i class="fas fa-times"></i>
                                </button>
                            </div>
                            <div class="toast-body">${notif.body}</div>
                        </div>`
                    );
                    $(`.toast#${notif.id}`)
                    .on("hide.bs.toast", _ => {
                        var shown = getShownNotifications();
                        shown.push(notif.id);
                        localStorage.setItem("shownNotifications", JSON.stringify(shown));
                    })
                    .toast("show");
                });
            } else {
                console.warn("localStorage isn't supported in this browser, notifications won't show.");
            };
        } else {
            console.error("Couldn't find valid notifications!")
        };
    })
    .fail((_, textStatus) => {
        console.error(`Notifications GET failed: "${textStatus}".`);
    });
});