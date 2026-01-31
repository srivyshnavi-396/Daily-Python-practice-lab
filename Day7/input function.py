{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8d58af54",
   "metadata": {},
   "source": [
    "input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "767052c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''The `input()` function is Python’s built-in way of talking to the user.\n",
    " It pauses program execution and waits for the user to type something on their keyboard and press **Enter**.'''\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "978014ff",
   "metadata": {},
   "source": [
    "string input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d1ac747a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sri\n"
     ]
    }
   ],
   "source": [
    "str = input(\"enter your name:\")\n",
    "print(str)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31ae7c12",
   "metadata": {},
   "source": [
    "int input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c20a8d89",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m age \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter your age:\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mstr\u001b[39m)\n",
      "File \u001b[1;32mc:\\Users\\srira\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1282\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1280\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1281\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1282\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_input_request(\n\u001b[0;32m   1283\u001b[0m     \u001b[38;5;28mstr\u001b[39m(prompt),\n\u001b[0;32m   1284\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parent_ident[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m   1285\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_parent(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1286\u001b[0m     password\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[0;32m   1287\u001b[0m )\n",
      "File \u001b[1;32mc:\\Users\\srira\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1325\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1322\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1323\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1324\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1325\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1326\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1327\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "age = int(input(\"enter your age:\"))\n",
    "print(str)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "356da76a",
   "metadata": {},
   "source": [
    "float input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8aec5cb4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m score \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mfloat\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mEnter youre score:\u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(score)\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: ''"
     ]
    }
   ],
   "source": [
    "score = float(input('Enter youre score:'))\n",
    "print(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7844cec4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# this is not working in vs jupyter so work in .py file\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52c1a91d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c322a91",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
