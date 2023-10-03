import chainlit as cl
from qa_bot_setup import qa_bot

@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Iniciando chat ....")
    await msg.send()
    msg.content = "Bienvenido, Hazme una pregunta "
    await msg.update()
    cl.user_session.set("chain", chain)

    @cl.on_message
    async def main(message):
        chain = cl.user_session.get("chain")
        cb = cl.AsyncLangchainCallbackHandler(
            stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
        )
        cb.answer_reached = True
        res = await chain.acall(message, callbacks=[cb])
        answer = res["result"]
        sources = res["source_documents"]

        if sources:
            answer += f"\nSources:" + str(sources)
        else:
            answer += f"\nNo Sources"
        await cl.Message(content=answer).send()
