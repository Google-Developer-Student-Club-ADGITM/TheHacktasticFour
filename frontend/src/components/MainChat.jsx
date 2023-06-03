import React from "react";
import ChatPane from "./ChatPane";
import ChatSelectPane from "./ChatSelectPane";
import "./mainChatCSS.css"
import Header from "./header";

function MainChat() {

    return (
        <div style={{display: "flex", height: "100vh", flexDirection: "column"}}>
            <Header />
            <div className="mainChatContainer">
                <ChatSelectPane />
                <ChatPane />
            </div>
        </div>
    )
}

export default MainChat;