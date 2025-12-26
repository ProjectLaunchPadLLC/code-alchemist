"use client";

import {
  createAssistant, // Creates an assistant that is aware of its past conversations.
  useCompletion, // Streams text from an LLM.
} from '@vercel/ai'

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'

import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

const INITIAL_INPUT = `My name is ${Math.random()}`;

export default function Index() {
  const {
    completion,
    input,
    isLoading,
    handleInputChange,
    handleSubmit,
    setInput,
  } = useCompletion({
    api: '/api/completion',
  })

  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      <div className="flex-1 p-4">
        <Card className="max-w-2xl mx-auto">
          <CardHeader>
            <CardTitle>AI Core Example</CardTitle>
            <CardDescription>
              This example shows how to use the AI Core package to stream
              responses from AI models.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center space-x-2">
                <Avatar>
                  <AvatarImage src="https://avatars.githubusercontent.com/u/14985020?v=4" />
                  <AvatarFallback>V</AvatarFallback>
                </Avatar>
                <div>
                  <p className="text-sm text-gray-500">You</p>
                  <p className="text-sm">{INITIAL_INPUT}</p>
                </div>
              </div>

              <div className="flex items-center space-x-2">
                <Avatar>
                  <AvatarImage src="/next.svg" />
                  <AvatarFallback>AI</AvatarFallback>
                </Avatar>
                <div>
                  <p className="text-sm text-gray-500">AI</p>
                  <p className="text-sm">{completion}</p>
                </div>
              </div>
            </div>
          </CardContent>
          <CardFooter className="space-x-2">
            <Input
              placeholder="Enter your prompt here..."
              value={input}
              onChange={handleInputChange}
            />
            <Button onClick={handleSubmit} disabled={isLoading}>
              {isLoading ? 'Loading...' : 'Send'}
            </Button>
          </CardFooter>
        </Card>
      </div>
      <footer className="flex items-center justify-center w-full h-24 border-t">
        <a
          className="flex items-center justify-center gap-2"
          href="https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=ai-sdk"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <img src="/vercel.svg" alt="Vercel Logo" className="h-4 ml-2" />
        </a>
      </footer>
    </div>
  )
}
