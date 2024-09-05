import 'vite/modulepreload-polyfill';

// Importation and configuration of HTMX
import htmx from "htmx.org";
window.htmx = htmx;

// Importation and configuration of Alpine.js
import Alpine from 'alpinejs';
window.Alpine = Alpine;
Alpine.start();

// Importation and configuration of Materialize.css
import "materialize-css";
M.AutoInit();

// Entry point for CSS styles
import "../styles/app.scss";

// Event handlers for modal-open and modal-close events
document.addEventListener("htmx:afterSwap", () => {
    M.AutoInit();
});

// Event handlers for modal-open and modal-close events
document.addEventListener("modal-open", () => {
    console.log("ouvrir la modale");
    const modal = document.getElementById("modal");
    if (modal) {
        M.Modal.getInstance(modal).open()
    }
});

document.addEventListener("modal-close", () => {
    const modal = document.getElementById("modal");
    if (modal) {
        M.Modal.getInstance(modal).close()
    }
});

