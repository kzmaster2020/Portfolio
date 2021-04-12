<template>
    <div>
        <p class="text-muted">
            <strong>{{answer.author}}</strong> &#8901; {{answer.created_at}}
        </p>
        <p>
            
        </p>
    </div>
    
</template>
<script>
export default {
    name: 'Answer',
    props: {
        answer: {
            type: Object,
            required: true
        }
    }
}
</script>