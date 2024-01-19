-- SQL script to set up chat and message tables for PostgreSQL

-- Create the 'chats' table
CREATE TABLE chats (
    id UUID PRIMARY KEY,         -- UUID for chat_id
    user_email VARCHAR(255),     -- Email address of the user
    title VARCHAR(255),          -- Title of the chat session
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of chat creation
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of chat creation
);

-- Create ENUM type for role
CREATE TYPE roles AS ENUM ('HUMAN', 'AI');

-- Create the 'messages' table
CREATE TABLE messages (
    id UUID PRIMARY KEY,                    -- UUID for message_id
    chat_id UUID REFERENCES chats(id), -- Chat ID, foreign key to the 'chats' table
    content TEXT,                           -- Content of the message
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,           -- Timestamp of the message
    role roles NOT NULL                     -- Role of the message sender
);

-- Create an index on the chat_id column of the messages table
CREATE INDEX idx_messages_chat_id ON messages(chat_id);
