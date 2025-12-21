hk
                const headerElement = document.getElementById("main-header");
            if (headerElement) {
                const currentPath = window.location.pathname;
                const isNavbarPage = currentPath.includes('/pages/navbar/');
                const headerPath = isNavbarPage ? "../header.html" : "pages/header.html";

                fetch(headerPath)
                    .then(response => response.text())
                    .then(data => {
                        headerElement.innerHTML = data;
                    })
                    .catch(error => {
                        console.error("Error fetching header:", error);
                    });
            }
        }

        document.addEventListener("DOMContentLoaded", addHeader);
