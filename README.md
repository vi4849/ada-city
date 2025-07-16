
# AdaCity
AdaCity is designed to bridge the gap between people with disabilities and communities. Using our image detection feature, users can upload photographs to learn about a location's accessibility.

Charlottesville, VA, with its rich historical heritage, presents unique challenges when it comes to accessibility. While the city's historical infrastructure contributes to its charm, it often falls short in accommodating people with disabilities. This problem inspired us to create AdaCity, a web application that aims to educate people on the accessibility of local places and help assess the accessibility infrastructure of these locations.

Our journey began with the realization that many UVA students with disabilities face daily challenges navigating a campus not originally designed with their needs in mind. We wanted to develop a solution that could make a tangible difference in our local community and beyond.

Through this project, we gained extensive knowledge about ADA compliance standards and the intricacies of accessible design. We were surprised to learn that, according to studies, approximately 65% of curb ramps and 48% of sidewalks are not accessible for people with disabilities.

One of our challenges was that our original model was not trained on images of sidewalks and streets and had a difficult time identifying the specific features and obstacles that impact accessibility. As a result, we pivoted to the Accessibility Object Detection model on Roboflow, which is specifically designed to identify and locate accessibility-related features in images of urban environments.

We built our web app using Python and the Django framework. The main feature of our web app is found in the Upload page of the website, where users can upload images of locations around the city to be analyzed by a computer vision machine learning model that identifies the presence or absence of accessibility-related objects like wheelchairs, ramps, stairs, doors, and elevators. We send the request with the image data using the API to the Accessibility Object Detection data annotation model on Roboflow. Then, the retrieved results are used to display the uploaded image with boxes around any accessibility objects that were detected, as well as a text description of the results and their confidence levels. Users can review these results to assess the accessibility of the location based on the detected features.

User uploaded images and analysis results are stored using Amazon S3. The results of past uploads are also stored in the user’s session, meaning they can look back on their previous results at any time.

Other features on our website include a Browse page, where users can view maps of accessible routes and ramp locations around UVA, as well as a list of ADA-compliant accessible parks in the Charlottesville area. Furthermore, an ADA Info page provides an overview of ADA standards for accessible infrastructure design.

A significant inspiration for AdaCity is its potential to assist schools as well as city and local governments in identifying areas that lack accessible infrastructure. By highlighting these existing gaps, we hope to inspire infrastructure development projects that will not only help equalize access for people with disabilities, but also boost local businesses by making them more accessible to a wider customer base and bringing their communities closer together.

Demo: https://www.youtube.com/watch?v=YRiaHPu2fio
