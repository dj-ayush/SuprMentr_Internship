# Assignment Date: 11/04/2026
# Assignment Name: Detection Brainstorm
# Description: List 5 uses of face/object detection and design one solution.


uses = [
    {
        "name": "Smartphone Face Unlock",
        "how": "A front camera captures the user's face; a CNN extracts "
               "facial embeddings and compares them with the stored one "
               "to unlock the device."
    },
    {
        "name": "Attendance Systems in Schools / Offices",
        "how": "A camera at the entrance detects faces and matches them "
               "against an employee/student database to mark attendance "
               "automatically."
    },
    {
        "name": "Self-Driving Cars",
        "how": "Object detection models (YOLO, SSD) identify pedestrians, "
               "vehicles, traffic signs, and lanes in real time so the car "
               "can react safely."
    },
    {
        "name": "Retail Analytics",
        "how": "Cameras in stores count visitors, detect queue lengths, "
               "and recognise products picked up by customers to improve "
               "layout and stock decisions."
    },
    {
        "name": "Medical Imaging",
        "how": "Object detection networks localise tumours or nodules in "
               "MRI / CT scans so radiologists can review faster."
    },
]


SOLUTION = """
=========================================================
 Proposed Solution : Smart School Bus Tracker
=========================================================

PROBLEM
  Parents worry about the safety of children during the school-bus
  commute. Manual attendance at the bus door is slow and error-prone.

IDEA
  Install a camera at the bus entry that uses face detection to confirm
  the identity of the boarding student and sends a notification to the
  parent's phone.

PIPELINE
  1. Camera at entry captures a short video stream.
  2. Face Detection (MediaPipe / YOLO-Face) locates each face.
  3. Face Recognition (FaceNet / ArcFace embeddings) matches the face
     against the pre-registered student list for that bus.
  4. System logs boarding/alighting events with timestamps.
  5. Cloud backend pushes an SMS / WhatsApp alert to the parent.

TECH STACK
  - Python + OpenCV + PyTorch (or TensorFlow Lite on edge devices).
  - Raspberry Pi 5 on the bus.
  - Cloud: Firebase / AWS Lambda for messaging.

PRIVACY
  - Store only face embeddings, not raw photos.
  - Process data on-device wherever possible.
  - Require explicit parental consent.
"""


def main() -> None:
    print("=== 5 Uses of Face / Object Detection ===\n")
    for i, u in enumerate(uses, 1):
        print(f"{i}. {u['name']}")
        print(f"   -> {u['how']}\n")

    print(SOLUTION)


if __name__ == "__main__":
    main()
