import React, { useState, useCallback, useRef, useEffect } from 'react'
import { useField } from '@unform/core'

import { Container, Input } from './styles'

export default function InputComponent({ name, message, icon: Icon,...rest }) {
    const inputRef = useRef(null)
    const { fieldName, defaultValue, error, registerField} = useField(name)

    const [isFocused, setIsFocused] = useState(false)
    const [isFilled, setIsFilled] = useState(false)

    const handleFocused = useCallback(() => {
        setIsFocused(true)
    }, [])

    const handleBlured = useCallback(() => {
        setIsFocused(false)
        setIsFilled(!!inputRef.current.value)
    }, [])


    useEffect(() => {
        registerField({
            name: fieldName,
            ref: inputRef.current,
            path: 'value'
        })
    }, [fieldName, registerField])

    return (
        <Container isFocused={isFocused} isFilled={isFilled}>
            {Icon && <Icon size={20} />}
                <Input 
                    {...rest}
                    ref={inputRef}
                    defaultValue={defaultValue}
                    placeholder={message}
                    onFocus={handleFocused}
                    onBlur={handleBlured}
                />
        </Container>
    )
}