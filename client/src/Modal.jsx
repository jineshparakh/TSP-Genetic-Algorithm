import { Center, Container, Modal, Space, Table } from '@mantine/core'
import React from 'react'


export default function MyModal({data, opened, setOpened}) {

  return (
    <Modal
    opened={opened}
    onClose={() => { setOpened(false)}}
    title="Algorithm result"
    size={'full'}
  >
   <Container>
    {opened ? (
      <>
        <Center>
        <img
          src={require(`./${data.plt}`)}
          alt="Algorithm Output"
          width={'50%'}
        />
      </Center>
       <Center>
       <Table horizontalSpacing="xs" verticalSpacing="xs" fontSize="md" width={"50%"} style={{textAlign:"center"}}>
            <thead>
                <tr>
                  <th style={{textAlign:"center"}}>Fittest Individual</th>
                  <th style={{textAlign:"center"}}>Fittest Route</th>
                </tr>
          </thead>

          {
            Object.values(data["Generation Data"]).map((d, idx) => (
              <tr key={idx}>
                <td>{d["Fittest Individual"]}</td>
                <td>{
                  d["Fittest Route"].length > 110
                  ? `${d["Fittest Route"].substring(0, 110)}…`
                  : d["Fittest Route"]
                }</td>
              </tr>
            ))
          }

        </Table>
       </Center>
       <Space h="md"/>
        <Center>
          Cost Array: {data["Cost"].toString()}
        </Center>
        <Space h="md"/>
        <Center>
          Minimum Distance Travelled: {data["Cost"].reduce((a,b)=>a+b)
}
        </Center>
      </>
     ) : null }
   </Container>
  </Modal>
  )
}
