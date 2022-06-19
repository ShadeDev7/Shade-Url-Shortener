const clipboard = document.getElementById("clipboard");
const outputUrl = document.getElementById("outputUrl");

if (clipboard && outputUrl) {
    clipboard.addEventListener("click", () => {
        const url = outputUrl.value;
        navigator.clipboard.writeText(url);

        outputUrl.value = "Copied!";

        setTimeout(() => {
            outputUrl.value = url;
        }, 2500);
    });
}
