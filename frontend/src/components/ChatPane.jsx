import React from "react";
import InputBox from "./chatPane/inputBox";
import MessageBox from "./chatPane/messageBox";

function ChatPane() {

    return (
        <div className="chatPaneContainer">
            <div className="introTextContainer">
                <h1>Start a new chat with wellness whiz!.</h1>
                <h3>Your personal healthcare chatbot</h3>
            </div>

            <div className="MessagesContainer">
                <MessageBox content={"lakslaklskalksksskdhhdhdhdhhdhdhdhdhhdhd        udud du du"} bot={false} />
                <MessageBox content={"huehuehue jeueujue hue"} bot={true} />
                <MessageBox content={"lakslaklskalksksskdhhdhdhdhhdhdhdhdhhdhd        udud du du"} bot={false} />
                <MessageBox content={"lakslaklskalksksskdhhdhdhdhhdhdhdhdhhdhd        udud du du"} bot={false} />
                <MessageBox content={"huehuehue jeueujue hue"} bot={true} />
                <MessageBox content={"huehuehue jeueujue hue"} bot={true} />
                <MessageBox content={"lakslaklskalksksskdhhdhdhdhhdhdhdhdhhdhd        udud du du"} bot={false} />
                <MessageBox content={"huehuehue jeueujue hue"} bot={true} />
            </div>

            <InputBox />
        </div>
    )
}

export default ChatPane;