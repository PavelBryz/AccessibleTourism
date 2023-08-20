# AccessibleTourism

This is proof of work source code of SPARK team's govHack2023 submission. 
Team members: Pavel Bryzgalov, Fiona Salimbangon, Chathuranga Jayasekara, Artyom Kurguzkin

# Ideas for the project
- Suggestion system
- Define accessibility of parks based on geo data
- AI voice guidance generation
- Website and mobile UI design prototype for disabled people

# Description

# Suggestion system
The suggestion system employs a two-step process to recommend suitable places of interest, tailored to individual user profiles and accessibility needs. It begins by filtering out places that aren't accessible to the specific user base, aligning with their defined preferences. For instance, if a place is inaccessible for wheelchairs, it's automatically excluded.

Following this initial filtration, the algorithm harnesses a k-nearest-neighbors approach to provide refined suggestions. It builds its recommendations on a foundation of accuracy-driven parameters, including elevation variations, the presence of amenities like public toilets, dedicated parking, as well as facilities catering to mobility and visual impairments. Additionally, user ratings and favorites contribute to shaping the suggestions.

The outcome of this intricate algorithm is a ranked assortment of places of interest, meticulously ordered according to their compatibility with the user's accessibility criteria. By blending verifiable parameters and user-centric data, the system ensures that its recommendations resonate with the unique needs of each user. Ultimately, this algorithm not only guides users towards intriguing destinations but also fosters inclusivity by fostering seamless exploration for individuals with diverse accessibility requirements.

# Define accessibility of parks based on geo data

Absolutely, considering the needs of people with disabilities, particularly those using wheelchairs, is essential. Terrain variations can significantly impact their ability to enjoy outdoor spaces. Here's the expanded explanation, still within 200 words:

The algorithm initiates by collecting park boundary data and Digital Elevation Models (DEM) data containing elevation values. Through data integration, a 2D array is constructed, associating elevation values with geographic points within park boundaries. This array is conceptually treated like an image.

Employing edge detection algorithms on this "elevation image" identifies abrupt elevation changes, signifying steep terrain. A quantitative elevation irregularity measure is derived, quantifying terrain roughness. Elevated measures denote heightened elevation disparities.

The algorithm interprets this metric to gauge the mobile accessibility of parks. For individuals with disabilities, particularly those using wheelchairs, navigating constantly ascending and descending terrains can transform a pleasant trip into a challenging ordeal. Parks with lower elevation irregularity metrics are deemed more wheelchair-accessible due to smoother terrain. Conversely, parks with higher metrics may present difficulties, potentially rendering them unsuitable for wheelchair users.

Ultimately, the algorithm classifies parks based on mobile suitability, with explicit consideration for people with disabilities. This comprehensive process, spanning data integration, edge detection, elevation metric computation, and mobile accessibility evaluation, furnishes insights into the impact of terrain on outdoor experiences, ensuring inclusive access for all park visitors.

# AI voice guidance generation

Upon activating the "Play Audio" button on the place of interest page, the algorithm initiates a comprehensive process. It begins by extracting the name of the selected place, leveraging it as a key identifier to gather information from diverse sources. Foremost among these sources is Wikipedia, which provides a foundational understanding of the place.

Drawing from this amalgamated data and taking into account the user's specific disability information, the algorithm formulates a nuanced and tailored prompt for ChatGPT, a conversational AI model. This prompt guides the AI in generating a response that encapsulates a rich description of the place, catering to the user's unique needs or disabilities.

The generated response is then seamlessly transferred to a voice creation system through an API interface. This interface triggers the process of transforming the textual content into a vocal representation. Notably, this vocal description is crafted to align with the user's disability, ensuring a comprehensive and meaningful auditory experience.

The overarching objective of this algorithm is to extend assistance to individuals who encounter challenges with visual information processing or those who prefer auditory formats. By furnishing auditory descriptions of places of interest, the algorithm fosters inclusivity, offering a valuable tool for those seeking information access through non-visual means.
