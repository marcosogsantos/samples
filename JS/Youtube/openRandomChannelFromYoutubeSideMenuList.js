function run() {
    let endpointElements = document.getElementsByClassName('yt-simple-endpoint style-scope ytd-guide-entry-renderer');
    let channels = [];
    for (let i = 0; i < endpointElements.length; i++) {
        let element = endpointElements[i]
        if (element.href.includes("channel")) {
            channels.push(element.href)
        }
    };
    endpointElements = undefined;
    for (let i = 0; i < 10; i++) {
    window.open(channels[Math.floor(Math.random() * channels.length)])
    }
}
run()