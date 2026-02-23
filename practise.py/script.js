//login
//get video list
//single video
console.log("starting...");
function login(email, password, cb) {
    setTimeout(() => {
        cb("login in process");
    }, 3000);
}

function getVideolist(user, cb) {
    setTimeout(() => {
        cb(["video1", "video2", "video3"]);
    }, 1000);
}

function getVideoDetails(video, cb) {
    setTimeout(() => {
        cb({ title: video, duration: "10 mins" });
    }, 1000);
}
//callback hell
login("user1", "password123", (data) => {
    console.log(data);
    getVideolist(data, (video) => {
        console.log(video);
        getVideoDetails(video[0], (details) => {
            console.log(details);
        });
    });
});