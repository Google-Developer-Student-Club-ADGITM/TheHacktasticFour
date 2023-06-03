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
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
                <MessageBox />
            </div>

            <InputBox />
        </div>
    )
}

export default ChatPane;