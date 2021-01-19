function pageScroll() {
    window.scrollBy(0,1);
    setTimeout(pageScroll,50);
}
pageScroll()