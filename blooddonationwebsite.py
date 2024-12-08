import streamlit as st
st.set_page_config(page_title="Blood Bank Network",page_icon=":drop_of_blood:",layout="wide")
with st.container():
    st.title('Be a Life Saver:anatomical_heart: For Someone "DONATE BLOOD":drop_of_blood:')
    st.write("---")
with st.container():
    st.subheader("Our Motto:dart:")
    st.write("No one should suffer or die due to lack of blood in their difficult times.")
    st.write("Serving the people by making Blood available when needed.")
    st.write("---")
with st.container():
    st.subheader("Reason to create this Website:exclamation:")
    st.write("Due to shortage of Blood for every month nearly 10,000 people are suffering in India.")
    st.write("It is difficult for the seeker to search for the Blood Donor in his/her difficult times this website makes it easy to find.")
    st.write("Even after raising the Blood request it takes nearly 1 to 2 days to get Blood.")
    st.write("Nearly 1 lakh unit of blood is getting wasted due to lack of coordination.")
    st.write("---")
with st.container():
    st.subheader("Advantage of Using This Website")
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("Search for Near by Donors:round_pushpin:")
        st.write("As this website provides complete information of Blood Donors so that the seekers can easily find near by donor which will be helpful for the Blood Seeker to get blood in time.")
    with right_column:
        st.write("##")
        st.subheader("Improve Coordination:family:")
        st.write("An online system can make it easier for donors and requesters to coordinate,which can lead to faster access to blood for those in need.")
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("Crisis Response")
        st.write("During Emergency this Website can quickly mobilize donors and coordinate Blood collection efforts to meet urgent needs.")
    with right_column:
        st.write("##")
        st.subheader("Real Time Connection")
        st.write("This website connects the Blood Donors and Blood Seekers on real time which reduces time,this time saving can save many lives.")
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("Increased Awareness:loudspeaker:")
        st.write("Website can raise awareness about the importance of Blood donation and the constant need for the Blood supplies.")
    with right_column:
        st.write("##")
        st.subheader("Simplified Searching Process:footprints:")
        st.write("Collection of data about Blood donors makes the searching process simpler for Blood seekers than traditional methods.")
    st.write("---")
with st.container():
    st.subheader("Eligibility Criteria for Donors:page_with_curl:")
    st.write("AGE : Donors must be between 18 to 65 years old.")
    st.write("WEIGHT : Donors must weigh atleast 45-50kg.")
    st.write("HEMOGLOBIN : Donors must have a hemoglobin level of atleast 12.5g/dL.")
    st.write("HEALTH : Donars shoud be in good health and free of infection such as cold,flu,sore throat etc...")
    st.write("BLOOD PRESSURE : Donors should have a normal blood pressure.")
    st.write("PULSE : Donors must have a pluse rate of 50-100 beats per minute.")
    st.write("---")
with st.container():
    st.subheader("Use this Website in proper way:warning:")
    st.write("Remember that Blood Donation is a Life-saving act so be considerate of others and use the website responsibly.")
    st.write("Be honest when filling the google forms.")
    st.write("Avoid making False requests.")
    st.write("---")
with st.container():
    st.subheader("DONATE BLOOD by clicking here:point_right:[click here>](https://forms.gle/J7gDxzrac7CuLsH18)")
    st.write("---")
with st.container():
    st.subheader("SEARCH FOR DONOR by clicking here:point_right:[click here>](https://docs.google.com/spreadsheets/d/1u2N0q62rfufeh65mF_6sRM5mO9PJtxoTfif7SqQJUNI/edit?resourcekey=&gid=616101134#gid=616101134)")
    st.write("---")
with st.container():
    st.subheader("Get in touch with me")
    st.write("If you find any error while using this website send me a mail")
    st.write("If you have any idea to update this website send me a mail")
    contact_form="""<form action="https://formsubmit.co/namalivaishnavi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>"""
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
st.balloons()
