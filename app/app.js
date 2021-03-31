// eel.expose(test_method);

// function test_method(test_input) {
//   console.log(">>> logging test: " + test_input);
// }

// test_method("THIS IS A TEST INPUT");
// eel.test_method("THIS IS A TEST INPUT FOR PYTHON");

let Application = document.createElement("div");
Application.className = "application";

let ApplicationFeatures = document.createElement("div");
ApplicationFeatures.className = "section";
ApplicationFeatures.innerHTML = `
<div class="option_card">
  <h3 class="option_title">Analyze Everything</h3>
  <button class="get_option_button non-decorated">Check Status</button>
</div>
<div class="option_card">
  <h3 class="option_title">Analyze Commands Usage</h3>
  <button class="get_option_button non-decorated">Check Status</button>
</div>
<div class="option_card">
  <h3 class="option_title">Analyze User Status</h3>
  <button class="get_option_button non-decorated">Check Status</button>
</div>
`;

Application.append(ApplicationFeatures);


let notification = document.createElement("div");
notification.className = "notification";
notification.innerHTML = `
<h2 class="notification-title">Want to Contribute to this Project?</h2>
<p class="notification-description">This is just a personal project of mine, but if you want to help/contribute, you are invited! Let's do some work together</p>
<button class="secondaryButton_Notification" onclick="window.open('https://www.github.com/yashsehgal/designsystem-bot/')">Check Source Code on GitHub</button>
`;

Application.appendChild(notification);



document.getElementById("application").appendChild(Application);




/// FEATURES FOR THE BOT ANALYTICS

const getCommandUsageDetails = function getCommandUsageDetails() {
  /// code here for command-usage-details
}

const getSpecialFeatureAnalytics = function getSpecialFeatureAnalytics() {
  /// code here for special feature usage details
}

const getCompleteAnalysis = function getCompleteAnalysis() {
  /// code here for complete analysis
}




/**
 * Tasks to implement
 * 
 * TODO: To make all the features DOM based and Dynamic
 * 
 * ? Keep code instances as consistent as possible for multi-purpose usage
 * ? Maintain all the python directories and in-directly connect all the python modules to the JS file and 
 * ? Keep the data-frames secure. This will help us to easily manipulate the methods over the python datasets.
 * ? All the datasets are having there duplicate files which will be used for analysis.
 * ? Python EEL linking will be done inside every method to make sure that the data-frames are accessed by right modules.
 * 
 * ! Keep code consistent, variable names should be meaningful
 */