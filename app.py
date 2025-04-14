import streamlit as st
from actors import get_sample_actors
from proposal import Proposal
from crisis import get_core_team, crisis_override

# Session State Initialization
if 'actors' not in st.session_state:
    st.session_state.actors = get_sample_actors()

if 'proposal' not in st.session_state:
    st.session_state.proposal = None

if 'system_state' not in st.session_state:
    st.session_state.system_state = 'design'

if 'phase_updated' not in st.session_state:
    st.session_state.phase_updated = False

st.title("🎓 EduChain: Blockchain Governance Simulation")
st.subheader(f"📌 Current Phase: {st.session_state.system_state.upper()}")

# Show Actors Table
st.markdown("### 👥 Actor List")
actors_data = [[a.name, a.role, a.tokens] for a in st.session_state.actors]
st.table({"Name": [row[0] for row in actors_data], "Role": [row[1] for row in actors_data], "Tokens": [row[2] for row in actors_data]})

# Create Proposal
if st.session_state.proposal is None:
    st.markdown("### 🧾 New Proposal")
    proposer = st.selectbox("Who is proposing?", [a.name for a in st.session_state.actors])
    proposal_text = st.text_input("Proposal Text:")
    if st.button("Submit Proposal") and proposal_text:
        proposer_actor = next(a for a in st.session_state.actors if a.name == proposer)
        st.session_state.proposal = Proposal(proposer_actor, proposal_text)
        proposer_actor.reward(2)
        st.success("Proposal created and proposer rewarded!")
        st.rerun()

# Voting Interface
elif st.session_state.system_state == "operate":
    st.markdown(f"### 🗳️ Voting on Proposal: *{st.session_state.proposal.text}*")
    for actor in st.session_state.actors:
        if actor.name != st.session_state.proposal.proposer.name and not actor.voted:
            vote = st.radio(f"{actor.name} ({actor.role}) Vote:", ["yes", "no"], key=actor.name)
            if st.button(f"Submit Vote - {actor.name}", key=actor.name+"_btn"):
                st.session_state.proposal.vote(actor, vote)
                actor.reward(1)
                st.success(f"{actor.name} voted '{vote}' and was rewarded.")
                st.rerun()

    if st.button("Finalize Voting"):
        result = st.session_state.proposal.result()
        if result == "accepted":
            st.success("🎉 Proposal ACCEPTED!")
        elif result == "rejected":
            st.error("❌ Proposal REJECTED!")
        elif result == "tie":
            st.warning("⚠️ TIE — No decision (might trigger crisis handling!)")
            st.session_state.system_state = "crisis"
        else:
            st.warning("⚠️ Unknown result.")
        st.session_state.phase_updated = True

# Design Phase
elif st.session_state.system_state == "design":
    st.markdown(f"### ⚙️ Design Phase Decision for Proposal: *{st.session_state.proposal.text}*")
    admin_decision = st.radio("Admin Decision:", ["yes", "no"])
    if st.button("Submit Admin Decision"):
        if admin_decision == "yes":
            st.success("✅ Admin APPROVED the proposal directly.")
        else:
            st.error("❌ Admin REJECTED the proposal directly.")
        st.session_state.system_state = "operate"
        st.session_state.phase_updated = True
        st.rerun()

# Crisis Phase
elif st.session_state.system_state == "crisis":
    st.markdown(f"### 🚨 Crisis: No Consensus for Proposal *{st.session_state.proposal.text}*")
    core_team = get_core_team(st.session_state.actors)
    st.markdown("**Core Team:** " + ", ".join([f"{m.name} ({m.role})" for m in core_team]))
    override_decision = st.radio("Core Team Override Decision:", ["yes", "no"])
    if st.button("Submit Core Team Decision"):
        result_msg = crisis_override(st.session_state.proposal, override_decision)
        if "APPROVED" in result_msg:
            st.success(result_msg)
        elif "REJECTED" in result_msg:
            st.error(result_msg)
        else:
            st.warning(result_msg)
        st.session_state.system_state = "operate"
        st.session_state.phase_updated = False
        st.session_state.proposal = None
        st.rerun()

# Reset
if st.button("🔁 Start New Proposal Round"):
    for a in st.session_state.actors:
        a.voted = False
    st.session_state.proposal = None
    st.session_state.phase_updated = False
    st.rerun()
