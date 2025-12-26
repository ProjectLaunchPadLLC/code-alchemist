import { createAssistant } from '@vercel/ai'

export const runtime = 'edge'

export async function POST(req: Request) {
  const assistant = await createAssistant({
    name: 'My Assistant',
  })

  const response = await assistant.completion({ stream: true, messages: [{ content: await req.text(), role: 'user' }] })

  return response
}
