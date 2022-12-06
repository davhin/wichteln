import streamlit as st
import utils as ut


st.set_page_config(page_title="Wichteln", page_icon="🎁")
st.title("Secret Gift Exchange")
st.write("Do a secret santa style gift exchange with a group of friends, family, or colleagues!")
with st.expander("How it works"):
    st.write("""
        This is an app for a secret santa style gift exchange that works like this:
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.header("A - Reveal Your Recipient")
recipient_code = st.text_input("Get the name of the lucky person who receives a gift from you!")
if recipient_code == "":
    st.write("Enter your code (e.g. WMXQB) above")
else:
    recipient_name = ut.get_gift_recipient(recipient_code)
    st.write(f"You need to get a gift for {recipient_name}!")


st.header("B - Create Gift Exchange")
st.subheader("Enter participant names")
text_names = st.text_input("names_text", label_visibility='collapsed')
names = ut.convert_text_to_names(text_names)
if not names:
  st.warning('Please input names, e.g. Alice, Eve, Bob')
  st.stop()
st.success('Thank you for inputting names.')
names_constraints = {name: [] for name in names}

st.subheader("Specify constraints")
st.write("For each person, select who they will not receive a gift from")

for name in names:
    col1, col2 = st.columns([1, 3])
    col1.write(name)
    names_constraints[name] = col2.multiselect(label="excl", options=[n for n in names if n != name], key=name, label_visibility='collapsed')
st.json(names_constraints)
solution = ut.solve(names_constraints)
if solution:
    st.write("Solution found!")
    st.json(solution)
else:
    st.write("No solution found. Maybe remove some constraints?")

st.subheader("Confirm & Download")
names_pseudonyms = dict(zip(names, ut.get_n_random_identifiers(len(names))))
print(names_pseudonyms)
ut.insert_solution_in_db(names_pseudonyms)
solution = {name:names_pseudonyms[solution[name]] for name in solution.keys()}
st.json(solution)