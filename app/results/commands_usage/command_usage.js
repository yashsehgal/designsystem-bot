

let command_usage_page = document.createElement("div");
command_usage_page.className = "page";

let command_usage_status_container = document.createElement("div");
command_usage_status_container.className = "section command_usage_status_section";
command_usage_status_container.innerHTML = `
  <img src="./commands_usage_plot.png" />
`;

command_usage_page.appendChild(command_usage_status_container);

document.getElementById("root").appendChild(command_usage_page);