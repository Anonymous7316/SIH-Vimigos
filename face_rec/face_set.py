import face_recognition
import cv2
import numpy as np
import win32com.client as wincl
list1 = []

speak = wincl.Dispatch("SAPI.SpVoice")
spk = speak.Speak
def face_rec_main():
    video_capture = cv2.VideoCapture(0)

    sat_image = face_recognition.load_image_file("face_rec/known_faces/satyaa.jpg")
    sat_face_encoding = face_recognition.face_encodings(sat_image)[0]

    sim_image = face_recognition.load_image_file("face_rec/known_faces/sim.jpg")
    sim_face_encoding = face_recognition.face_encodings(sim_image)[0]

    ut_image = face_recognition.load_image_file("face_rec/known_faces/utkarsh.jpg")
    ut_face_encoding = face_recognition.face_encodings(ut_image)[0]

    ek_image = face_recognition.load_image_file("face_rec/known_faces/ekansh.jpg")
    ek_face_encoding = face_recognition.face_encodings(ek_image)[0]
    
    he_image = face_recognition.load_image_file("face_rec/known_faces/hemang.jpg")
    he_face_encoding = face_recognition.face_encodings(he_image)[0]

    dh_image = face_recognition.load_image_file("face_rec/known_faces/dhawal.jpg")
    dh_face_encoding = face_recognition.face_encodings(dh_image)[0]

    known_face_encodings = [
        sat_face_encoding,
        sim_face_encoding,
        ut_face_encoding,
        ek_face_encoding,
        he_face_encoding,
        dh_face_encoding

    ]
    known_face_names = [
        "Satyaa ",
        "Simran ",
        "Utkarsh ",
        "Ekansh ",
        "Hemang ",
        "Dhawal "
    ]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
    

    while True:
        idx=0
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    if name not in list1:
                        list1.append(name)
                        spk(f"{name} has arrived")
                        print(name+" has arived")
                    
    
                idx += 1
                print (idx)
                face_names.append(name)

        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            


            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(list1)
            return list1
            break

    video_capture.release()
    cv2.destroyAllWindows()

