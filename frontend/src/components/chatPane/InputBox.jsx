import React from "react";

function InputBox() {

    return (
        <div className="InputBoxContainer">
            <div className="InputFormHolder">

                <form style={{ display: "flex" }}>
                    <input type="text" placeholder="Ask your query..." className="InputBox"></input>
                    <button type="submit">send</button>
                </form>
            </div>
        </div>
    )
}

export default InputBox;